        ## Overview
        
        Based on template by Richard Kavanagh
        https://github.com/zabbix/community-templates/tree/main/Server_Hardware/Other/template_nvidia-smi_integration
        
        This template integrates NVidia SMI for any number of graphic cards with Zabbix.
        
        The template adds monitoring of:
        
        * GPU Utilisation
        * GPU Power Consumption
        * GPU Memory (Used, Free, Total)
        * GPU Temperature
        * GPU Fan Speed
        
        The following agent parameters can be used to add the metrics into Zabbix:
        
        UserParameter=gpu.discovery,nvidia-smi -L | grep -Eo "GPU-[a-z0-9-]*" | sed 's/.*/{"{#GPUID}":"&"}/;1s/^/[/;$!s/$/,/;$s/$/]/' | tr -d '\n'
        UserParameter=gpu.temp[*],nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits -i $1
        UserParameter=gpu.memtotal[*],nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits -i $1
        UserParameter=gpu.used[*],nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i $1
        UserParameter=gpu.free[*],nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits -i $1
        UserParameter=gpu.fanspeed[*],nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits -i $1
        UserParameter=gpu.utilisation[*],nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits -i $1
        UserParameter=gpu.power[*],nvidia-smi --query-gpu=power.draw --format=csv,noheader,nounits -i $1
        
        ## Author
        Theodor Zurabishvili

