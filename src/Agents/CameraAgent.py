"""
An simple agent to instantiate Minibot(Third).

@author: FATESAIKOU
@date  : 06/26/2018
"""

import numpy as np
import requests
import base64
import json
import io

from PIL import Image

class CameraAgent:
    def __init__( self, api_url ):
        self.is_constructed = False
        self.SetUrl(api_url)


    """ Initialization """
    def GetUrl( self ):
        return self.__api_url;

    def SetUrl( self, api_url ):
        try:
            camera_resp = requests.get( api_url )
            self.CheckResponse(camera_resp)

            self.__api_url = api_url
            self.camera_status = self.BuildCameraStatus(camera_resp)
            self.is_constructed = True
        except Exception as e:
            print('Unable to set url as "' + api_url + '"\n' + str(e))


    """ Get Status """
    def GetStatus( self, fresh = False ):
        if fresh or not hasattr(self, 'camera_status'):
            camera_resp = requests.get( self.__api_url )
            self.CheckResponse(camera_resp)

            self.camera_status = self.BuildCameraStatus(camera_resp)
        
        return self.camera_status

    def SaveImg( self, filename ):
        camera_resp = requests.get( self.__api_url )
        self.CheckResponse(camera_resp)

        self.camera_status = self.BuildCameraStatus(camera_resp, filename)
        
        return self.camera_status



    """ Utils """
    def CheckResponse( self, response ):
        if (response.status_code != 200):
            raise SystemError('Server responses with bad status code: ' + str(response.status_code))

    def BuildCameraStatus( self, response, filename = None):
        tmp_obj = json.loads(response.content)

        if ('image_b64' not in tmp_obj.keys()):
            return None

        byte_str = base64.b64decode( tmp_obj['image_b64'] )
        image = Image.open(io.BytesIO( byte_str ))
        image_data = np.array(image)

        if (filename != None):
            image.save(filename)

        return {'image': image_data}

