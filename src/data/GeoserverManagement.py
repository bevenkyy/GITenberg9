#-*- coding:utf-8 -*-

import os
import subprocess
import json

class GeoserverManagement:

    def __init__(self, host, port, username, password, curl_bin_dir):
        #
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        #
        os.chdir(curl_bin_dir)

    def _parse_response_data(self, response_data):
        '''
        '''
        json_obj = None
        if len(response_data) == 0:
            return json_obj
        else:
            json_str = response_data[0]
            json_obj = json.loads(json_str)
        #
        return json_obj

    def get_workspace_name(self):
        '''
        获取所有工作空间名称
        '''
        workspace_name = []
        #
        cmd = 'curl -v -u ' + self.username+ ':' + self.password + \
              ' -X GET -H "Accept: application/json" http://' + self.host + ':' + \
              self.port + '/geoserver/rest/workspaces/'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        #
        response_data = sub_process.stdout.readlines()
        json_data = self._parse_response_data(response_data)
        if json_data != None:
            workspaces_list = json_data.get("workspaces")
            if type(workspaces_list) == dict:
                workspace_list = workspaces_list.get("workspace")
                for workspace_dict in workspace_list:
                    workspace_name.append(workspace_dict.get("name"))
        #
        sub_process.wait()
        #
        return workspace_name

    def get_style_name(self):
        '''
        获取所有样式名称
        '''
        style_name = []
        #
        cmd = 'curl -v -u ' + self.username+ ':' + self.password + \
              ' -X GET -H "Accept: application/json" http://' + self.host + ':' + \
              self.port + '/geoserver/rest/styles/'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        #
        response_data = sub_process.stdout.readlines()
        json_data = self._parse_response_data(response_data)
        if json_data != None:
            styles_list = json_data.get("styles")
            if type(styles_list) == dict:
                style_list = styles_list.get("style")
                for style_dict in style_list:
                    style_name.append(style_dict.get("name"))
        #
        sub_process.wait()
        #
        return style_name

    def get_datastore_name(self, workspace_name):
        '''
        获取所有数据存储名称
        '''
        datastore_name = []
        #
        cmd = 'curl -v -u ' + self.username+ ':' + self.password + \
              ' -X GET -H "Accept: application/json" http://' + self.host + ':' + \
              self.port + '/geoserver/rest/workspaces/' + workspace_name + '/datastores/'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        #
        response_data = sub_process.stdout.readlines()
        json_data = self._parse_response_data(response_data)
        if json_data != None:
            datastores_list = json_data.get("dataStores")
            if type(datastores_list) == dict:
                datastore_list = datastores_list.get("dataStore")
                for datastore_dict in datastore_list:
                    datastore_name.append(datastore_dict.get("name"))
        #
        sub_process.wait()
        #
        return datastore_name

    def create_workspace(self, workspace_name):
        '''
        创建工作空间
        ''' 
        cmd = 'curl -v -u ' + self.username+ ':' + self.password + \
              ' -X POST -H "Content-type: text/xml" -d "<workspace><name>' + workspace_name + \
              '</name></workspace>" http://' + self.host + ':' + self.port + '/geoserver/rest/workspaces/'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        sub_process.wait()  

    def publish_geotiff(self, geotiff_filepath, workspace_name, layer_name):
        '''
        发布（上传）GeoTiff文件
        ''' 
        cmd = 'curl -u ' + self.username+ ':' + self.password + \
              ' -X PUT -H "Content-type:image/tiff" --data-binary @"'+ \
              geotiff_filepath + '" http://' + self.host + ':' + self.port + '/geoserver/rest/workspaces/' + \
              workspace_name + '/coveragestores/' + layer_name + '/file.geotiff'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        sub_process.wait()

    def create_style(self, style_filepath, style_name):
        '''
        创建样式目录并上传样式文件
        ''' 
        cmd = 'curl -u ' + self.username+ ':' + self.password + \
              ' -X POST -H "Content-type: text/xml" -d "<style><name>' + style_name + \
              '</name><filename>' + style_name + '</filename></style>" http://' + self.host + ':' + \
              self.port + '/geoserver/rest/styles/'
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        sub_process.wait()
        #
        ####
        #
        cmd = 'curl -u ' + self.username+ ':' + self.password + \
              ' -X PUT -H "Content-type: application/vnd.ogc.sld+xml" -d @"' + style_filepath + \
              '" http://' + self.host + ':' + self.port + '/geoserver/rest/styles/' + style_name
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        sub_process.wait()

    def apply_style(self, style_name, workspace_name, layer_name):
        '''
        应用指定样式到指定图层
        ''' 
        cmd = 'curl -u ' + self.username+ ':' + self.password + \
              ' -X PUT -H "Content-type: text/xml" -d "<layer><defaultStyle><name>' + style_name +\
              '</name></defaultStyle><enabled>true</enabled></layer>" http://' + self.host + ':' + self.port + \
              '/geoserver/rest/layers/' + workspace_name + ':' + layer_name
        #
        sub_process = subprocess.Popen(cmd,
                                       stdout = subprocess.PIPE,
                                       stderr = subprocess.PIPE,
                                       universal_newlines = True)
        sub_process.wait()