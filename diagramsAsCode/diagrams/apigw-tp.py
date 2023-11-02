
from diagrams import Diagram,Cluster,Edge
from diagrams.custom          import Custom
from diagrams.generic.network import Firewall
from diagrams.oci.network     import LoadBalancer
from urllib.request           import urlretrieve

# You can change the data flow direction with direction parameter. Default is LR.
# (TB, BT, LR and RL) are allowed.

with Diagram("API Gateway and Threat Protection in Green and Red Zones", show=True, filename="apigw-tp",direction="TB" ):

  # Software AG Cloud
  cloud_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Software_AG_Cloud-256x256.png"
  cloud_icon = "Software_AG_Cloud-256x256.png.tmp"
  urlretrieve(cloud_url, cloud_icon)

  # API Gateway
  apigw_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_API_Gateway-256x256.png"
  apigw_icon = "webMethods_API_Gateway-256x256.png.tmp"
  urlretrieve(apigw_url, apigw_icon)

  i = Custom("Internet", cloud_icon)

  with Cluster("Red Zone (DMZ)" ):
    f01 = Firewall("Firewall")
    tp  = Custom("Threat Protection", apigw_icon)

  with Cluster("Green Zone" ):
    f02 = Firewall("Firewall")
    a   = Custom("API Gateway", apigw_icon)

  i >> f01 >> tp << Edge(label="polls") << f02 << Edge(label="polls") << a
