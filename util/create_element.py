##Creates HTML for each item that has been modified or added for email##
def create_element(type, item):
    return (
        f'<div style="display:inline-block;height:380px;width:250px;border:1px solid #a4dcdb;border-radius:5px;margin:0 10px 10px 0;vertical-align:top;">'
        f'<div style="height:60%;width:100%">'
        f'<img style="display:block;height:175px;margin:0 auto;padding-top:25px"src="{item["img"]}">'
        f'</div>'
        f'<div style="height:40%;width:100%;background-color:#f9f9f9;border-radius:0 0 5px 5px">'
        f'<div style="width:100%;height:60%;text-align:center;display:table">'
        f'<span style="display:table-cell;vertical-align:middle;font-size:19px;">{item["name"]}</span>'
        f'</div>'
        f'<div style="width:100%;height:40%">'
        f'<a href="{item["link"]}"style="display:table;text-decoration:none;text-align:center;width:60%;height:30px;background-color:#4496df;color:white;margin:15px auto 0 auto;border-radius:3px">'
        f'<span style="display:table-cell;vertical-align:middle;font-size:15px;">{type}</span>'
        f'</a>'
        f'</div>'
        f'</div>'
        f'</div>'
    )