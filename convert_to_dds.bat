@echo off

REM Check if an image file is dragged onto the batch file
IF [%1]==[] (
    echo No image file specified.
    echo Drag and drop an image file onto this batch file to convert it to DDS format.
    pause
    exit /b 1
)

REM Set the input and output file paths
set "input=%~1"
set "output=%~dpn1.dds"

REM Run nvcompress command with the specified options
nvcompress -color -mipfilter kaiser -bc1 "%input%" "%output%"

REM Check if the conversion was successful
IF %errorlevel% equ 0 (
    echo Conversion completed successfully.
    exit /b 0
) else (
    echo Conversion failed.
    exit /b 1
)