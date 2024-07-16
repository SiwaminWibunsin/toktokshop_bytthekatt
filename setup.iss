[Setup]
AppName=TikTok Shop Bot
AppVersion=1.0
DefaultDirName={pf}\TikTokShopBot
DefaultGroupName=TikTok Shop Bot
OutputDir=.
OutputBaseFilename=TikTokShopBotSetup

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\TikTok Shop Bot"; Filename: "{app}\main.exe"
Name: "{group}\Uninstall TikTok Shop Bot"; Filename: "{uninstallexe}"
