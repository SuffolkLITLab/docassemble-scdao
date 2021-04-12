from docassemble.base.util import CustomDataType, DAValidationError, word
import re

class Charges(CustomDataType):
    name = 'charges'
    container_class = 'da-charges-container'
    input_class = 'magicsearch multi'
    #input_type = 'charges'
    javascript = """\
    var dataSource;
    if(dataSource){
        $(document).on('daPageLoad', function(){
            $(".magicsearch").magicsearch({
                dataSource: dataSource,
                multiple: true,
                fields: ["firstName","lastName"],
                multiField: "firstName",
                hidden:true,
                id:"id",
                format:"%firstName% · %lastName%"
            });
        });
        $.validator.addMethod('charges', function(value, element, params){
            return true;
        });
    };
    """

    is_object = True
    jq_rule = 'Charges'
    jq_message = 'You need to enter the charges.'

    @classmethod
    def validate(cls, item):
        return True

    @classmethod
    def transform(cls, item):
        dataSource1 = [
            {'firstName':'MURDER, FIRST DEGREE  c. 265 s. 1', 'lastName':'c. 265 s. 2(a)'},
            {'firstName':'TREASON', 'lastName':'c. 264 s. 2'},
            {'firstName':'MURDER, FIRST DEGREE BY A MINOR c. 265 s. 1', 'lastName':'c. 265 s. 2(b) and c. 279 s. 24'},
            {'firstName':'A&B, AGGRAVATED, SERIOUS BODILY INJURY c. 265 s. 13A(b)(i)', 'lastName':'c. 265 s. 13A(b)(i)'},
            {'firstName':'A&B TO COLLECT LOAN c. 265 s. 13C', 'lastName':'c. 265 s. 13C'},
            {'firstName':'MURDER, ATTEMPTED c. 265 s. 16', 'lastName':'c. 265 s. 16'},
            {'firstName':'ROBBERY, ARMED, FIREARM c. 265 s. 17', 'lastName':'c. 265 s. 17'},
            {'firstName':'ROBBERY, ARMED, FIREARM & MASKED c. 265 s. 17', 'lastName':'c. 265 s. 17'},
            {'firstName':'STALKING, SUBSQ. OFF. c. 265 s. 43(c)', 'lastName':'c. 265 s. 43(c)'},
            {'firstName':'FIRE, LARCENY AT c. 266 s. 23', 'lastName':'c. 266 s. 24'},
        ]
        returnValue = []
        for selection in item.split(","):
            ds=dataSource[int(selection)+1]
            returnValue.append(ds['firstName']+' '+ds['lastName'])
        return returnValue
