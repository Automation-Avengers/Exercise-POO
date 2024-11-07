$exclude = @("venv", "BotFuncionario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotFuncionario.zip" -Force