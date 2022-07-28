import requests

class TestApi(object):
    file_name = ""
    def test_fileList(self):
        url = "https://otaplanner.ou.nsn-rdnet.net/api/datastorage/v3/fileList"
        data = {
            "linkDirection" : "uplink",
            "standard" : "5gnr",
            "duplexMode" : "tdd",
            "tddFrameConfiguration" : "dl_special_ul_dl_special_ul_3_1_1_2_1_2",
            "physicalCellId" : 1,
            "bandwidthMhz" : 100,
            "testmodelName" : "g-fr1-a2-5",
            "subCarrierSpacingKhz" : 30,
            "rank" : 1,
            "antenna" : 0,
        }
        res = requests.get(url=url,params=data,verify=False)
        result = res.json()["fileList"][0]
        TestApi.file_name = result["devices"]["generator"][2]["fileName"]
        print(type(result),result)


    def test_downloadFile(self):

        url = "https://otaplanner.ou.nsn-rdnet.net/api/datastorage/v3/downloadFile"
        fileName = TestApi.file_name
        res = requests.get(url,params=fileName,verify=False)
        result = res.json()
        print(result)
