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

#安装控制器elasticsearch-servicewrapper
#如果是在服务器上就可以使用elasticsearch-servicewrapper这个es插件，它支持通过参数，指定是在后台或前台运行es，并且支持启动，停止，重启es服务（默认es脚本只能通过ctrl+c关闭es）。
#使用方法是到https://github.com/elasticsearch/elasticsearch-servicewrapper下载service文件夹，放到es的bin目录下。下面是命令集合：
#bin/service/elasticsearch +console 
#在前台运行esstart 在后台运行esstop 停止esinstall 使es作为服务在服务器启动时自动启动remove 取消启动时自动启动
#vim /usr/local/elasticsearch/service/elasticsearch.conf
#set.default.ES_HOME=/usr/local/elasticsearch

#查看状态
http://localhost:9200/_status?pretty=true
#查看集群健康
http://localhost:9200/_cat/health?v
#列出集群索引
http://localhost:9200/_cat/indices?v
#删除索引
curl -XDELETE ‘http://localhost:9200/kibana-int/’
curl -XDELETE ‘http://localhost:9200/logstash-2015.10.*’
#优化索引
curl -XPOST ‘http://localhost:9200/old-index-name/_optimize’

