
from diagrams import Diagram,Cluster,Edge
from diagrams.custom          import Custom
from diagrams.generic.network import Firewall
from diagrams.oci.network     import LoadBalancer
from urllib.request           import urlretrieve
from diagrams.elastic.elasticsearch import Elasticsearch

# You can change the data flow direction with direction parameter. Default is LR.
# (TB, BT, LR and RL) are allowed.

with Diagram("API Gateway and Threat Protection in Cluster", show=True, filename="apigw-tp-cluster",direction="TB" ):

  # Software AG Cloud
  cloud_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Software_AG_Cloud-256x256.png"
  cloud_icon = "Software_AG_Cloud-256x256.png.tmp"
  urlretrieve(cloud_url, cloud_icon)

  # API Gateway
  apigw_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_API_Gateway-256x256.png"
  apigw_icon = "webMethods_API_Gateway-256x256.png.tmp"
  urlretrieve(apigw_url, apigw_icon)

  i = Custom("Internet", cloud_icon)

  with Cluster("Red Zone (DMZ)"):
    f01   = Firewall("Firewall")
    lb    = LoadBalancer("Load Balancer")
    tp01  = Custom("Threat Protection 01", apigw_icon)
    tp02  = Custom("Threat Protection 02", apigw_icon)

  with Cluster("Green Zone"):
    with Cluster("API Gateway Cluster" ):
      a01 = Custom("API Gateway 01", apigw_icon)
      a02 = Custom("API Gateway 02", apigw_icon)
      a03 = Custom("API Gateway 03", apigw_icon)

    with Cluster("Elasticsearch Cluster"):
      e01 = Elasticsearch("Elasticsearch 01")
      e02 = Elasticsearch("Elasticsearch 02")
      e03 = Elasticsearch("Elasticsearch 03")

  i >> f01 >> lb >> [tp01, tp02]
  [tp01, tp02] << a01
  [tp01, tp02] << a02
  [tp01, tp02] << a03
  
  a01 - e01
  a02 - e02
  a03 - e03