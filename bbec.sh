#!/bin/bash

#
# Pre-flight checks
#

SOURCEDIR=$1
REGEX=$2
EXPDIR=$3
EXPFORMAT=$4
EXECSOURCE=$5

BEPY=$(realpath ./batchexport.py)
VALID_EXPFORMATS=("fbx" "obj" "x3d" "gltf")

if [ "$SOURCEDIR" = "" ];
then
	echo "Error: No source directory specified!"
	exit 1
fi

if [ "$REGEX" = "" ];
then
	echo "Error: No regex specified!"
	exit 1
fi

if [ "$EXPDIR" = "" ];
then
	echo "Error: No export directory specified!"
	exit 1
fi

if [[ ! " ${VALID_EXPFORMATS[*]} " =~ " ${EXPFORMAT,,} " ]]; then
	echo "Error: Unknown export format ${EXPFORMAT}! Valid formats are:"
	for f in "${VALID_EXPFORMATS[@]}"; do
		echo $f
	done
	exit 1
fi

if [ "$EXECSOURCE" = "" ];
then
	echo "Warn: No executable source specified, using default command (blender -b ...). If you are using Blender's Flatpak version, use './recursive_export.sh <regex> <export directory> <export format> flatpak'."
fi

if [ "$BEPY" = "" ];
then
	echo "Error: Could not locate batchexport.py!"
	exit 1
fi


#
# Resolve blender files recursively
#

echo "Looking for Blender files using regex ${REGEX}.blend..."

readarray -d '' blenderfiles < <(find ~+ "${SOURCEDIR}" -type f -name "${REGEX}.blend" -print0)


if [ ${#blenderfiles[@]} -eq 0 ]; then
    echo "No Blender files found."
    exit
fi


#
# Report findings
#

echo "${#blenderfiles[@]} Blender files found:"
for bf in "${blenderfiles[@]}"; do
    echo $bf
done


#
# Do the actually important stuff
#

echo "Ensuring export directory existence..."
mkdir -p $EXPDIR

echo "Exporting models..."

export BBEC_EXPORT_FORMAT="${EXPFORMAT}"

for bf in "${blenderfiles[@]}"; do
	BF_DIRNAME=$(dirname "${bf}")
	BF_EXPDIR=${EXPDIR}/${BF_DIRNAME/$SOURCEDIR/}
	
	export BBEC_EXPORT_PATH=$BF_EXPDIR
	
	mkdir -p "${BF_EXPDIR}"

	if [ "${EXECSOURCE,,}" = "flatpak" ];
	then
		flatpak run org.blender.Blender -b "${bf}" --python $BEPY
	else
    		blender -b "${bf}" --python $BEPY
	fi
done


#
# Cleanup
#

exit
