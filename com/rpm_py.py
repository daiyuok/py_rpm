#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson


def jump():
    print ("show me your code!!! \n")
    paramss = {
        "ati": "42152504182",
        "certi_id": "1873901138",
        "date": "2017-03-27 11:02:12",
        "format": "json",
        "from_api_v": "2.2",
        "from_node_id": "1635313936",
        "method": "store.trade.fullinfo.get",
        "node_type": "suning",
        "tid": "36140254710",
        "to_node_id": "1833323732",
        "userId": "admin",
        "userIp": "27.115.50.210",
    }

    print simplejson.dumps(paramss)

if __name__ == '__main__':
    jump()
