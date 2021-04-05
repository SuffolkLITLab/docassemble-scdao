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
        #ds=datasource[int(item)]
        #return ds.firstName+' '+ds.lastName
        return item


