import httpx
import json
class API:
	def __init__(self,ApiKey,Version):self._h='https://app.cybertkr.com';self._get=httpx.Client(http2=True,timeout=120);self.api_key=ApiKey;self.api_version=Version;self.headers={'ApiKey':self.api_key,'API-Version':self.api_version}
	def GoodPrint(self,jsonpack):print(json.dumps(jsonpack,indent=4))
	def _appuseragent(self,App):istek=self._get.post(self._h+'/'+self.api_version+'/appname?App='+App,headers=self.headers).json();return istek
	def _apprandom(self):istek=self._get.post(self._h+'/'+self.api_version+'/apprandom',headers=self.headers).json();return istek
	def _weatherapi(self,location):istek=self._get.post(self._h+'/'+self.api_version+'/weatherapi?Location='+location,headers=self.headers).json();return istek
	def _instaprofile(self,username):istek=self._get.post(self._h+'/'+self.api_version+'/instagramapi/instasearch?Parameters='+username,headers=self.headers).json();return istek
	def _screenShotWeb(self,query):istek=self._get.post(self._h+'/'+self.api_version+'/webscreenshot?Parameters='+query,headers=self.headers);return istek
	def _covid19(self,countrycode):istek=self._get.post(self._h+'/'+self.api_version+'/covid19api?Parameters='+countrycode,headers=self.headers);return istek
	def _tiktoksearch(self,username):istek=self._get.post(self._h+'/'+self.api_version+'/tiktokapi?Parameters='+username,headers=self.headers);return istek
	def _lineqr(self,appname,UserAgent):self.headers['AppName']=appname;self.headers['UserAgent']=UserAgent;istek=json.loads(self._get.post(self._h+'/'+self.api_version+'/qrCode',headers=self.headers).text);return istek
	def _linepin(self,key,session,appname,userAgent):self.headers['AppName']=appname;self.headers['UserAgent']=userAgent;istek=json.loads(self._get.post(self._h+'/'+self.api_version+'/Pincode'+'/'+key+'/'+session,headers=self.headers).text);return istek
	def _lineauthToken(self,key,session,appname,userAgent):self.headers['AppName']=appname;self.headers['UserAgent']=userAgent;istek=json.loads(self._get.post(self._h+'/'+self.api_version+'/authToken'+'/'+key+'/'+session,headers=self.headers).text);return istek
