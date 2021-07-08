import huaweisms.api.common


XML_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<request>"
    "<dataswitch>{enable}</dataswitch>"
    "</request>"
)

XML_NET_MODE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<request>"
    "<NetworkMode>{}</NetworkMode>"
    "<NetworkBand>3FFFFFFF</NetworkBand>"
    "<LTEBand>7FFFFFFFFFFFFFFF</LTEBand>"
    "</request>"
)

def connect_mobile(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    return switch_mobile_on(ctx)


def disconnect_mobile(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    return switch_mobile_off(ctx)


def get_mobile_status(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    result = huaweisms.api.common.get_from_url(url, ctx)
    if result and result.get("type") == "response":
        response = result["response"]
        if response and response.get("dataswitch") == "1":
            return "CONNECTED"
        if response and response.get("dataswitch") == "0":
            return "DISCONNECTED"
    return "UNKNOWN"


def switch_mobile_off(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    data = XML_TEMPLATE.format(enable=0)
    headers = {
        "__RequestVerificationToken": ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)


def switch_mobile_on(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    data = XML_TEMPLATE.format(enable=1)
    headers = {
        "__RequestVerificationToken": ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)

def set_network_mode(ctx, net):
    """ net value 
    00 AUTO
    01 EDGE
    02 WCDMA
    03 LTE
    """
    data = XML_NET_MODE.format(net)
    headers = {
        "__RequestVerificationToken": ctx.token,
    }

    url = "{}/net/net-mode".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)
