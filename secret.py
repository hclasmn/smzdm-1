### 是否弃用微信 server酱 推送

IS_USE_WX_PUSH = False

FT_QQ_KEY = ''

### 是否启动qq推送  请 前往 https://wx.scjtqs.com/qq/user 配置qq并获取token
IS_USE_QQ_PUSH = os.environ["PUSH_ON"]

PUSH_QQ = 0   ###### 个人qq推送

PUSH_GROUP = os.environ["PUSH_GROUP"]  ###### qq群推送

PUSH_TOKEN = os.environ["PUSH_TOKEN"]   ###### qq推送秘钥


