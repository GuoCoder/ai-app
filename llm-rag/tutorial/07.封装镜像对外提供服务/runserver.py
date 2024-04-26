# -*- coding: utf-8 -*-   
import uvicorn,sys  
from opsapp.app.main import get_application, get_para
app = get_application()
# -------------------- 业务 --------------------   
from app import  router as application

app.include_router(application) 

     
if __name__ == '__main__':
    host, port = get_para()
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    port = 10090
    uvicorn.run(app='__main__:app', host=host, port=port, reload=True)
