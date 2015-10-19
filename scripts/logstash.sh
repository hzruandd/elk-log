#Download and install the Public Signing Key:
wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
#Add the repository definition to /etc/apt/sources.list file:
echo "deb http://packages.elasticsearch.org/logstash/1.5/debian stable main" | sudo tee -a /etc/apt/sources.list
#update and install
sudo apt-get update && sudo apt-get install logstash


