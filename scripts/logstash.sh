#Download and install the Public Signing Key:
wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
#Add the repository definition to /etc/apt/sources.list file:
echo "deb http://packages.elasticsearch.org/logstash/1.5/debian stable main" | sudo tee -a /etc/apt/sources.list
#update and install
sudo apt-get update && sudo apt-get install logstash


#查看本机现在有多少插件可用,(其实就在 vendor/bundle/jruby/1.9/gems/ 目录下
bin/plugin install logstash-output-newplugin
#升级已有插件
bin/plugin update logstash-input-tcp
#本地插件安装这对自定义插件或者无外接网络的环境都非常有效：
#执行成功以后。你会发现，logstash-1.5.0 目录下的 Gemfile 文件最后会多出一段内容
bin/plugin install /path/to/logstash-filter-crash.gem
