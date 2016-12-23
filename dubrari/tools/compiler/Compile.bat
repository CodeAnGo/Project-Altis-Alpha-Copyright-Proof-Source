@echo off
echo ################################
echo #    Dubito's PDNA Compiler    #
echo ################################
echo #        June 23th 2013        #
echo ################################
rem  Updated July 30th 2013 # For Toontown House
rem  Updated October 22nd 2013 # For Toontown House
rem  Updated Feburary 12th 2014 # For Toontown Transformed
rem  Updated November 03rd 2014 # For Toontown Transformed
rem  Updated December 07th 2016 # For Project Altis
rem  Updated December 08th 2016 # For Project Altis
set /P inpFile="What file would you like to compile (With Extension)?: " || ^
set inpFile=X
set /P outFile="What should the compiled file be called (No Extension)?: " || ^
set outFile=X
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
echo Starting Compilation of %inpFile%.
rem replace my panda python path with yours! (Should be future compatible)
..\..\..\Panda3D-1.10.0\python\python.exe compile.py --output Output\%outFile%.pdna %inpFile% --verbose --compress
echo =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
pause