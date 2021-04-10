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
        dataSource = [
            {'firstName':'Tim', 'lastName':'Cook'},
            {'firstName':'Eric', 'lastName':'Baker'},
            {'firstName':'Victor', 'lastName':'Brown'},
            {'firstName':'Lisa', 'lastName':'White'},
            {'firstName':'Oliver', 'lastName':'Bull'},
            {'firstName':'Zade', 'lastName':'Stock'},
            {'firstName':'David', 'lastName':'Reed'},
            {'firstName':'George', 'lastName':'Hand'},
            {'firstName':'Tony', 'lastName':'Well'},
            {'firstName':'Bruce', 'lastName':'Wayne'},
        ]
        returnValue = []
        for selection in item.split(","):
            ds=dataSource[int(selection)+1]
            returnValue.append(ds['firstName']+' '+ds['lastName'])
        return returnValue