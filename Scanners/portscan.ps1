<#     
    .NOTES 
    =========================================================================== 
     Created with:     SAPIEN Technologies, Inc., PowerShell Studio 2018 v5.5.149 
     Created on:       5/5/2018 17:25 
     Created by:       Lex van der Horst 
     Organization:     TechEdge 
     Filename:         PS-Port-Scanner.ps1 
    =========================================================================== 
    .DESCRIPTION 
        This PowerShell script is extremely useful when you are behind a firewall,  
        and you are running service on a remote machine that you want to connect to it,  
        but you are unable to find out which ports can be accessed and to which port 
        to bind the service. 
#> 
 
$host.ui.RawUI.WindowTitle = "PowerShell Port Scanner" 
 
# Select a port range 
$PortRange = 0 .. 10000

$net="172.30.0"
$range=1..254 
 
foreach($r in $range){
    
    $ip="{0}.{1}" -F $net,$r    
    Write-Host "Checking: $ip"
    # Open connection for each port from the PortRange 
    foreach ($Port in $PortRange) 
    { 
        $Socket = New-Object Net.Sockets.TcpClient 
        $ErrorActionPreference = 'SilentlyContinue' 
        # Connect on the given port
        $Socket.Connect($ip, $Port) 
        # Determine if the connection is established 
        if ($Socket.Connected) 
        { 
            Write-Host "Outbound port $Port is open." -ForegroundColor Green 
            $Socket.Close() 
        } 
    }
} 
