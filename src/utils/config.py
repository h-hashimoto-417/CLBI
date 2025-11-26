# -*-coding:utf-8-*-

import sys

# --------------------------------
# Code Path
# --------------------------------
# This variable should be modified as the correct path when running code in other locations.
CODE_PATH = '/Users/hashimoto/Githubrepo/research_project_b4/CLBI/'
sys.path.append(CODE_PATH)

# --------------------------------
# Testing
# --------------------------------
# is it a test run?
# test runs reduce the dataset to 1 test release
TEST = False

# --------------------------------
# Cached Result
# --------------------------------
# Do we use the cached results? True=yes(False=no) means that speed up the prediction process.
USE_CACHE = False

# --------------------------------
# Dataset project
# --------------------------------
# 時系列順に並べたreleases
# PROJECT_RELEASE_LIST = [

#     'ambari-1.2.0', 'ambari-2.1.0', 'ambari-2.2.0', 'ambari-2.4.0', 'ambari-2.5.0', 'ambari-2.6.0', 'ambari-2.7.0',
#     'amq-5.0.0', 'amq-5.1.0', 'amq-5.2.0', 'amq-5.4.0', 'amq-5.5.0', 'amq-5.6.0', 'amq-5.7.0', 'amq-5.8.0',
#     'amq-5.9.0', 'amq-5.10.0', 'amq-5.11.0', 'amq-5.12.0', 'amq-5.14.0', 'amq-5.15.0',
#     'bookkeeper-4.0.0', 'bookkeeper-4.2.0', 'bookkeeper-4.4.0',
#     'calcite-1.6.0', 'calcite-1.8.0', 'calcite-1.11.0', 'calcite-1.13.0',
#     'calcite-1.15.0', 'calcite-1.16.0', 'calcite-1.17.0', 'calcite-1.18.0',
#     'cassandra-0.7.4', 'cassandra-0.8.6', 'cassandra-1.0.9', 'cassandra-1.1.6', 'cassandra-1.1.11', 'cassandra-1.2.11',
#     'flink-1.4.0', 'flink-1.6.0',
#     'groovy-1.0', 'groovy-1.5.5', 'groovy-1.6.0', 'groovy-1.7.3', 'groovy-1.7.6', 'groovy-1.8.1', 'groovy-1.8.7',
#     'groovy-2.1.0', 'groovy-2.1.6', 'groovy-2.4.4', 'groovy-2.4.6', 'groovy-2.4.8', 'groovy-2.5.0', 'groovy-2.5.5',
#     'hbase-0.94.1', 'hbase-0.94.5', 'hbase-0.98.0', 'hbase-0.98.5', 'hbase-0.98.11',
#     'hive-0.14.0', 'hive-1.2.0', 'hive-2.0.0', 'hive-2.1.0',
#     'ignite-1.0.0', 'ignite-1.4.0', 'ignite-1.6.0',
#     'log4j2-2.0', 'log4j2-2.1', 'log4j2-2.2', 'log4j2-2.3', 'log4j2-2.4', 'log4j2-2.5', 'log4j2-2.6', 'log4j2-2.7',
#     'log4j2-2.8', 'log4j2-2.9', 'log4j2-2.10',
#     'mahout-0.3', 'mahout-0.4', 'mahout-0.5', 'mahout-0.6', 'mahout-0.7', 'mahout-0.8',
#     'mng-3.0.0', 'mng-3.1.0', 'mng-3.2.0', 'mng-3.3.0', 'mng-3.5.0', 'mng-3.6.0',
#     'nifi-0.4.0', 'nifi-1.2.0', 'nifi-1.5.0', 'nifi-1.8.0',
#     'nutch-1.1', 'nutch-1.3', 'nutch-1.4', 'nutch-1.5', 'nutch-1.6', 'nutch-1.7', 'nutch-1.8', 'nutch-1.9',
#     'nutch-1.10', 'nutch-1.12', 'nutch-1.13', 'nutch-1.14', 'nutch-1.15',
#     'storm-0.9.0', 'storm-0.9.3', 'storm-1.0.0', 'storm-1.0.3', 'storm-1.0.5',
#     'tika-0.7', 'tika-0.8', 'tika-0.9', 'tika-0.10', 'tika-1.1', 'tika-1.3', 'tika-1.5', 'tika-1.7', 'tika-1.10',
#     'tika-1.13', 'tika-1.15', 'tika-1.17',
#     'ww-2.0.0', 'ww-2.0.5', 'ww-2.0.10', 'ww-2.1.1', 'ww-2.1.3', 'ww-2.1.7', 'ww-2.2.0', 'ww-2.2.2', 'ww-2.3.1',
#     'ww-2.3.4', 'ww-2.3.10', 'ww-2.3.15', 'ww-2.3.17', 'ww-2.3.20', 'ww-2.3.24',
#     'zookeeper-3.4.6', 'zookeeper-3.5.1', 'zookeeper-3.5.2', 'zookeeper-3.5.3',

# ]

PROJECT_RELEASE_LIST = [
    'spring-projects.spring-boot-1.0.0',
    'iluwatar.java-design-patterns-1.0.0',
    'square.retrofit-1.0.0',
    'square.okhttp-1.0.0',
    #'zxing.zxing-1.0.0',
    'libgdx.libgdx-1.0.0',
    'google.guava-1.0.0',
    'alibaba.dubbo-1.0.0',
    'jfeinstein10.SlidingMenu-1.0.0',
    'netty.netty-1.0.0',
    'JakeWharton.ActionBarSherlock-1.0.0',
    'chrisbanes.Android-PullToRefresh-1.0.0',
    'alibaba.fastjson-1.0.0',
    'deeplearning4j.deeplearning4j-1.0.0',
    #'JakeWharton.ViewPagerIndicator-1.0.0',
    'alibaba.druid-1.0.0',
    #'liaohuqiu.android-Ultra-Pull-To-Refresh-1.0.0',
    'mybatis.mybatis-3-1.0.0',
    'springside.springside4-1.0.0',
    'apache.storm-1.0.0',
    'xetorthio.jedis-1.0.0',
    'apache.hadoop-1.0.0',
    'dropwizard.dropwizard-1.0.0',
    'swagger-api.swagger-codegen-1.0.0',
    'code4craft.webmagic-1.0.0',
    'junit-team.junit-1.0.0',
    'Trinea.android-common-1.0.0',
    'clojure.clojure-1.0.0',
    'nhaarman.ListViewAnimations-1.0.0',
    'perwendel.spark-1.0.0',
    #'spring-projects.spring-mvc-showcase-1.0.0',
    'square.dagger-1.0.0',
    'swagger-api.swagger-core-1.0.0',
    'jhy.jsoup-1.0.0',
    'mcxiaoke.android-volley-1.0.0',
    'Activiti.Activiti-1.0.0',
    #'spring-projects.spring-petclinic-1.0.0',
    'openhab.openhab-1.0.0',
    'JakeWharton.NineOldAndroids-1.0.0',
    'wildfly.wildfly-1.0.0',
    'Bukkit.Bukkit-1.0.0',
    #'jersey.jersey-1.0.0',
    'NLPchina.ansj_seg-1.0.0',
    'spring-projects.spring-security-oauth-1.0.0',
    'eclipse.vert.x-1.0.0',
    'apache.flink-1.0.0',
    'neo4j.neo4j-1.0.0',
    'google.guice-1.0.0',
    #'MyCATApache.Mycat-Server-1.0.0',
    'apache.camel-1.0.0',
    'druid-io.druid-1.0.0',
    'naver.pinpoint-1.0.0',
    'AsyncHttpClient.async-http-client-1.0.0',
    'thinkaurelius.titan-1.0.0',
    'stanfordnlp.CoreNLP-1.0.0',
    #'dropwizard.metrics-1.0.0',
    'bauerca.drag-sort-listview-1.0.0',
    'EnterpriseQualityCoding.FizzBuzzEnterpriseEdition-1.0.0',
    'brettwooldridge.HikariCP-1.0.0',
    'pardom.ActiveAndroid-1.0.0',
    'google.auto-1.0.0',
    #'square.otto-1.0.0',
    'openmrs.openmrs-core-1.0.0',
    'alibaba.jstorm-1.0.0',
    #'b3log.solo-1.0.0',
    'hankcs.HanLP-1.0.0',
    'knightliao.disconf-1.0.0',
    'facebook.presto-1.0.0',
    'aws.aws-sdk-java-1.0.0',
    'cucumber.cucumber-jvm-1.0.0',
    'Atmosphere.atmosphere-1.0.0',
    'yusuke.twitter4j-1.0.0',
    'yasserg.crawler4j-1.0.0',
    'alibaba.canal-1.0.0',
    'gephi.gephi-1.0.0',
    'NanoHttpd.nanohttpd-1.0.0',
    'google.closure-compiler-1.0.0',
    #'JakeWharton.DiskLruCache-1.0.0',
    'apache.hive-1.0.0',
    #'square.okio-1.0.0',
    'scribejava.scribejava-1.0.0',
    #'checkstyle.checkstyle-1.0.0',
    'roboguice.roboguice-1.0.0',
    'hazelcast.hazelcast-1.0.0',
    'antlr.antlr4-1.0.0',
    #'databricks.learning-spark-1.0.0',
    'Alluxio.alluxio-1.0.0',
    #'jfinal.jfinal-1.0.0',
    'apache.hbase-1.0.0',
    'javaee-samples.javaee7-samples-1.0.0',
    'joelittlejohn.jsonschema2pojo-1.0.0',
    #'dangdangdotcom.elastic-job-1.0.0',
    'pxb1988.dex2jar-1.0.0',
    #'alibaba.DataX-1.0.0',
    #'shuzheng.zheng-1.0.0',
    'Graylog2.graylog2-server-1.0.0',
    'brianfrankcooper.YCSB-1.0.0',
    #'essentials.Essentials-1.0.0',
    #'kbastani.spring-cloud-microservice-example-1.0.0',
    'square.javapoet-1.0.0'

]

# --------------------------------
# DO NOT CHANGE FROM HERE ON
# --------------------------------

# Let's change some parameters (i.e., make them smaller) if this is a test run
if TEST:
    PROJECT_RELEASE_LIST = ['ambari-1.2.0', 'ambari-2.1.0', 'ambari-2.2.0', 'ambari-2.4.0']
