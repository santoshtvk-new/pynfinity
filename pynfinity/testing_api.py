import datetime
import json
from os.path import join, dirname

from flask import jsonify, Response

courses_json_reference = join(dirname(__file__), "static/content/courses.json")


def name_of_parent(dict_json_body, data_type):
    parent = [i for i in dict_json_body.keys() if dict_json_body[i]['icon'] == data_type]
    if not parent:
        parent = [i for i in dict_json_body.keys() if dict_json_body[i]['icon'] == data_type + '.svg']
    return parent[0]


def different_responses_api(request, data_type, sc):
    str_json_body = open(courses_json_reference).read()
    dict_json_body = json.loads(str_json_body)
    json_body = jsonify(dict_json_body)
    if request.method == 'GET':
        if data_type == "json":
            return json_body, sc
        if data_type == "text":
            return ("Get response with text format is successful! Here's sample long text: Automation describes a wide "
                    "range of technologies that reduce human intervention in processes, mainly by predetermining "
                    "decision criteria, subprocess relationships, and related actions, as well as embodying those "
                    "predeterminations in machines. Automation has been achieved by various means including "
                    "mechanical, hydraulic, pneumatic, electrical, electronic devices, and computers, usually in "
                    "combination. Complicated systems, such as modern factories, airplanes, and ships typically use "
                    "combinations of all of these techniques. The benefit of automation includes labor savings, "
                    "reducing waste, savings in electricity costs, savings in material costs, and improvements to "
                    "quality, accuracy, and precision."), sc
        if data_type == 'xml':
            xml_data = """
    <?xml version="1.0"?>
    <catalog>
       <book id="bk101">
          <author>Gambardella, Matthew</author>
          <title>XML Developer's Guide</title>
          <genre>Computer</genre>
          <price>44.95</price>
          <publish_date>2000-10-01</publish_date>
          <description>An in-depth look at creating applications 
          with XML.</description>
       </book>
       <book id="bk102">
          <author>Ralls, Kim</author>
          <title>Midnight Rain</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-12-16</publish_date>
          <description>A former architect battles corporate zombies, 
          an evil sorceress, and her own childhood to become queen 
          of the world.</description>
       </book>
       <book id="bk103">
          <author>Corets, Eva</author>
          <title>Maeve Ascendant</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-11-17</publish_date>
          <description>After the collapse of a nanotechnology 
          society in England, the young survivors lay the 
          foundation for a new society.</description>
       </book>
       <book id="bk104">
          <author>Corets, Eva</author>
          <title>Oberon's Legacy</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2001-03-10</publish_date>
          <description>In post-apocalypse England, the mysterious 
          agent known only as Oberon helps to create a new life 
          for the inhabitants of London. Sequel to Maeve 
          Ascendant.</description>
       </book>
       <book id="bk105">
          <author>Corets, Eva</author>
          <title>The Sundered Grail</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2001-09-10</publish_date>
          <description>The two daughters of Maeve, half-sisters, 
          battle one another for control of England. Sequel to 
          Oberon's Legacy.</description>
       </book>
       <book id="bk106">
          <author>Randall, Cynthia</author>
          <title>Lover Birds</title>
          <genre>Romance</genre>
          <price>4.95</price>
          <publish_date>2000-09-02</publish_date>
          <description>When Carla meets Paul at an ornithology 
          conference, tempers fly as feathers get ruffled.</description>
       </book>
       <book id="bk107">
          <author>Thurman, Paula</author>
          <title>Splish Splash</title>
          <genre>Romance</genre>
          <price>4.95</price>
          <publish_date>2000-11-02</publish_date>
          <description>A deep sea diver finds true love twenty 
          thousand leagues beneath the sea.</description>
       </book>
       <book id="bk108">
          <author>Knorr, Stefan</author>
          <title>Creepy Crawlies</title>
          <genre>Horror</genre>
          <price>4.95</price>
          <publish_date>2000-12-06</publish_date>
          <description>An anthology of horror stories about roaches,
          centipedes, scorpions  and other insects.</description>
       </book>
       <book id="bk109">
          <author>Kress, Peter</author>
          <title>Paradox Lost</title>
          <genre>Science Fiction</genre>
          <price>6.95</price>
          <publish_date>2000-11-02</publish_date>
          <description>After an inadvertant trip through a Heisenberg
          Uncertainty Device, James Salway discovers the problems 
          of being quantum.</description>
       </book>
       <book id="bk110">
          <author>O'Brien, Tim</author>
          <title>Microsoft .NET: The Programming Bible</title>
          <genre>Computer</genre>
          <price>36.95</price>
          <publish_date>2000-12-09</publish_date>
          <description>Microsoft's .NET initiative is explored in 
          detail in this deep programmer's reference.</description>
       </book>
       <book id="bk111">
          <author>O'Brien, Tim</author>
          <title>MSXML3: A Comprehensive Guide</title>
          <genre>Computer</genre>
          <price>36.95</price>
          <publish_date>2000-12-01</publish_date>
          <description>The Microsoft MSXML3 parser is covered in 
          detail, with attention to XML DOM interfaces, XSLT processing, 
          SAX and more.</description>
       </book>
       <book id="bk112">
          <author>Galos, Mike</author>
          <title>Visual Studio 7: A Comprehensive Guide</title>
          <genre>Computer</genre>
          <price>49.95</price>
          <publish_date>2001-04-16</publish_date>
          <description>Microsoft Visual Studio 7 is explored in depth,
          looking at how Visual Basic, Visual C++, C#, and ASP+ are 
          integrated into a comprehensive development 
          environment.</description>
       </book>
    </catalog>
                """
            return Response(xml_data, mimetype='application/xml'), sc
        else:
            if str(data_type).upper().startswith("QP"):
                try:
                    res = {}
                    data_type = request.query_string.decode()
                    params = str(data_type).split('&')
                    for p in params:
                        k = p.split('=')[0]
                        v = p.split('=')[1]
                        res[k] = v
                    return res, sc
                except Exception as e:
                    return {
                        "Query Parameters": f"{str(data_type)}",
                        "Error": f"{e}",
                        "Message": "Check Query Parameters"
                    }, sc
            return {"DATATYPE": f"{str(data_type)}"}, sc
    if request.method == 'POST':
        new_body = {}
        print(">>", request.data)
        page_responses = request.get_json() if request.get_json() else "NO DATA"
        try:
            res = json.loads(str(page_responses))
            if 'file' in request.files and request.files['file'].filename != '' and request.files['file'] and \
                    str(request.files['file'].filename).rsplit['.', 1][-1] in ['txt', 'pdf', 'png', 'jpg', 'jpeg',
                                                                               'gif', 'csv', 'py', 'json']:
                new_body['file_name'] = request.files['file'].filename
                new_body['file_upload_status'] = "CONSIDERED BUT NOT-UPLOADED FOR SECURITY & MEMORY REASONS"
            new_body['input'] = res
            new_body['timestamp'] = str(datetime.datetime.now())
            new_body['status'] = 'success'
            return new_body, sc
        except Exception as e:
            new_body['input'] = str(page_responses)
            new_body['timestamp'] = str(datetime.datetime.now())
            new_body['status'] = 'success'
            return new_body, sc
    if request.method == 'PUT':
        page_responses = request.get_json() if request.get_json() else ""
        if page_responses:
            unique_ids = []
            for k in dict_json_body.keys():
                unique_ids.append(dict_json_body[k]['icon'])
                unique_ids.append(dict_json_body[k]['icon'].rsplit('.', 1)[0])

            if data_type in unique_ids:
                data_type = name_of_parent(dict_json_body, data_type)
                dict_json_body[data_type] = page_responses
                return jsonify(dict_json_body), sc
            else:
                return {
                    "error": f"{data_type} not in unique_identifier",
                    "unique_identifier": unique_ids
                }, sc
        else:
            return {"error": "No data to update"}, sc
    if request.method == 'PATCH':
        page_responses = request.get_json() if request.get_json() else {}
        if page_responses:
            unique_ids = []
            for k in dict_json_body.keys():
                unique_ids.append(dict_json_body[k]['icon'])
                unique_ids.append(dict_json_body[k]['icon'].rsplit('.', 1)[0])
            if data_type in unique_ids:
                try:
                    data_type = name_of_parent(dict_json_body, data_type)
                    for k in dict_json_body[data_type].keys():
                        if k in page_responses.keys():
                            dict_json_body[data_type][k] = page_responses[k]
                    return jsonify(dict_json_body), sc
                except Exception as e:
                    print(e)
            else:
                return {
                    "error": f"{data_type} not in unique_identifier",
                    "unique_identifier": unique_ids
                }, sc

        return {"error": "No data to update"}, sc

    if request.method == 'DELETE':
        unique_ids = []
        for k in dict_json_body.keys():
            unique_ids.append(dict_json_body[k]['icon'])
            unique_ids.append(dict_json_body[k]['icon'].rsplit('.', 1)[0])
        if data_type in unique_ids:
            data_type = name_of_parent(dict_json_body, data_type)
            del dict_json_body[data_type]
            return jsonify(dict_json_body), sc
        else:
            return {
                "error": f"{data_type} not in unique_identifier",
                "unique_identifier": unique_ids
            }, sc
    else:
        return {"error": "No data to delete"}, sc
