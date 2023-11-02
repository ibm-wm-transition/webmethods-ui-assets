from diagrams import Diagram, Cluster,Edge
from diagrams.custom import Custom
from urllib.request import urlretrieve

# You can change the data flow direction with direction parameter. Default is LR.
# (TB, BT, LR and RL) are allowed.
with Diagram("Software AG Product Icons", show=True, filename="sag-demo", direction="LR"):

  # Import Software AG icons, here is a subset ...
  
  # Adabas
  ada_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Adabas-256x256.png"
  ada_icon = "Adabas-256x256.png.tmp"
  urlretrieve(ada_url, ada_icon)

  # Alphabet
  alphabet_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Alfabet-256x256.png"
  alphabet_icon = "Alfabet-256x256.png.tmp"
  urlretrieve(alphabet_url, alphabet_icon)

  # ARIS
  aris_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/ARIS-256x256.png"
  aris_icon = "ARIS-256x256.png.tmp"
  urlretrieve(aris_url, aris_icon)

  # Cumulocity IoT
  c8y_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Cumulocity_IoT-256x256.png"
  c8y_icon = "Cumulocity_IoT-256x256.png.tmp"
  urlretrieve(c8y_url, c8y_icon)

  # Natural
  nat_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Natural-256x256.png"
  nat_icon = "Natural-256x256.png.tmp"
  urlretrieve(nat_url, nat_icon)
  
  # Software AG Cloud
  cloud_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/Software_AG_Cloud-256x256.png"
  cloud_icon = "Software_AG_Cloud-256x256.png.tmp"
  urlretrieve(cloud_url, cloud_icon)

  # API Control Plane
  apicp_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_API_Control_Plane-256x256.png"
  apicp_icon = "webMethods_API_Control_Plane-256x256.png.tmp"
  urlretrieve(apicp_url, apicp_icon)

  # API Gateway
  apigw_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_API_Gateway-256x256.png"
  apigw_icon = "webMethods_API_Gateway-256x256.png.tmp"
  urlretrieve(apigw_url, apigw_icon)

  # Developer Portal
  devpo_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_Developer_Portal-256x256.png"
  devpo_icon = "webMethods_Developer_Portal-256x256.png.tmp"
  urlretrieve(devpo_url, devpo_icon)

  # EntireX
  exx_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_EntireX-256x256.png"
  exx_icon = "webMethods_EntireX-256x256.png.tmp"
  urlretrieve(exx_url, exx_icon)

  # Integration Server
  is_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_Integration_Server-256x256.png"
  is_icon = "webMethods_Integration_Server-256x256.png.tmp"
  urlretrieve(is_url, is_icon)

  # MFT
  mft_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_MFT-256x256.png"
  mft_icon = "webMethods_MFT-256x256.png.tmp"
  urlretrieve(mft_url, mft_icon)

  # Microservices Runtime
  msr_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_Microservices_Runtime-256x256.png"
  msr_icon = "webMethods_Microservices_Runtime-256x256.png.tmp"
  urlretrieve(msr_url, msr_icon)

  # Universal Messaging
  um_url  = "https://github.com/SoftwareAG/webmethods-ui-assets/raw/main/product-icons/256x256/webMethods_Universal_Messaging-256x256.png"
  um_icon = "webMethods_Universal_Messaging-256x256.png.tmp"
  urlretrieve(um_url, um_icon)
  
  # ... end of importing

  # Now, we can draw ...
  aris      = Custom("ARIS",                  aris_icon)
  ada       = Custom("Adabas",                ada_icon)
  alphabet  = Custom("Alphabet",              alphabet_icon)
  c8y       = Custom("Cumulocity IoT",        c8y_icon) 
  nat       = Custom("Natural",               nat_icon)
  cloud     = Custom("Software AG Cloud",     cloud_icon)
  apicp     = Custom("API Control Plane",     apicp_icon)
  apigw     = Custom("API Gateway",           apigw_icon)
  devportal = Custom("Developer Portal",      devpo_icon)
  exx       = Custom("EntrireX",              exx_icon)
  is1       = Custom("Integration Server",    is_icon)
  mft       = Custom("MFT",                   mft_icon)
  msr       = Custom("Microservices Runtime", msr_icon)
  um        = Custom("Universal Messaging",   um_icon)
  
  ada   - Edge(color="none") - alphabet - Edge(color="none") - aris - Edge(color="none") - c8y - Edge(color="none") - nat - Edge(color="none") - cloud - Edge(color="none") - apicp
  apigw - Edge(color="none") - devportal - Edge(color="none") - exx - Edge(color="none") - is1 - Edge(color="none") - mft - Edge(color="none") - msr - Edge(color="none") - um
  
