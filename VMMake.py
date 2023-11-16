import requests
import json

url = "https://management.azure.com/subscriptions/304a1406-ae26-4fa5-9432-4ee53762d6d5/resourceGroups/VirtualMachineEuan_group/providers/Microsoft.Compute/virtualMachines/vm4?api-version=2023-07-01"

headers = {
  {
  "id": "/subscriptions/304a1406-ae26-4fa5-9432-4ee53762d6d5/resourceGroups/VirtualMachineEuan_group/ providers/Microsoft.Compute/virtualMachines/vm4",
  "type": "Microsoft.Compute/virtualMachines",
  "properties": {
    "osProfile": {
      "adminUsername": "euanm",
      "secrets": [
        
      ],
      "computerName": "vm4",
      "linuxConfiguration": {
        "ssh": {
          "publicKeys": [
            {
                 "path": "/home/euanm/.ssh/authorized_keys",
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/wslQAAXa3nLgSi5ffxNGufzlPKXjHBQ/n7ghJsJIWMM16LAbN0PdBu1Qx/fVckLD4usrvh/uOsbzbFiv5vWVsbyHYWDJ1g8lfhdxqRAwn7ip9w0fScLIAIQ9yZhVH3NIk0m2Y9FOSLWopei9d5efzxACiJRZqPOzZwO2Nzs+iD5qz7C5WTY/Ym8jW/W6/fbHxi+WXZFkOkmJ3tN170rx29m2xBKfESO60QWYUQzZIsYZX+aq8wcuzzoL0mTTnOyGvcUOhdKysmQwT8JReOThFKcGpxkYC4sc92tkhFeXf6zhtdfFlW1MtidvmCC+jJU3p8GuGXab+t2AMqIWkXO7d312RAB2um9SMwy1SfbSc/tqw9eM05CQ9/ASUHOq0Aj3BoSHyDTrbTKl1cx6O+D7QP60XLl1mMQ/jYS28Yeh9DvM1a/2iqDZfsZ+HmjgxU9UXvkHegBHpoKsYXAgZ8/irZDJlWTu2EqIZyAjONjPEKuzSvADqBE2S1zBOUPokbM= euanm@LAPTOP-TBBA52TH"
            }
          ]
        },
        "disablePasswordAuthentication": true
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/304a1406-ae26-4fa5-9432-4ee53762d6d5/resourceGroups/VirtualMachineEuan_group/ providers/Microsoft.Network/networkInterfaces/neti4",
          "properties": {
            "primary": true
          }
        }
      ]
    },
    "storageProfile": {
      "imageReference": {
        "sku": "16.04-LTS",
        "publisher": "Canonical",
        "version": "latest",
        "offer": "UbuntuServer"
      },
      "dataDisks": [
        
      ]
    },
    "hardwareProfile": {
      "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
  },
  "name": "vm4",
  "location": "eastus"
}
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())