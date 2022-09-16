#!/bin/bash

#
# Pre-flight checks
#

REGEX=$1
EXPDIR=$2
EXPFORMAT=$3
EXECSOURCE=$4

BEPY=$(realpath ./batchexport.py)

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

if [ "$EXPFORMAT" = "" ];
then
	echo "Error: No export format specified (e.g. fbx, obj, ...)!"
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

readarray -d '' blenderfiles < <(find ~+ . -type f -name "${REGEX}.blend" -print0)


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

export BBEC_EXPORT_PATH=$EXPDIR
export BBEC_EXPORT_FORMAT=".${EXPFORMAT}"

for bf in "${blenderfiles[@]}"; do
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
