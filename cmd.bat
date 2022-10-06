set folder=%1
echo nul > result.txt
copy /y nul  result.txt
IF EXIST %folder% (
   for /r %folder% %%A in (*.txt) do findstr /M /C:"In vino veritas!"  %%A  >> result.txt && echo[ >>result.txt
    ) ELSE (
        echo "„ ­­®© Ї ЇЄЁ ­Ґв"
    )

pause
