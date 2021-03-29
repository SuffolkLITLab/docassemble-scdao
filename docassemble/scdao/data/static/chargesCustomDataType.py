from docassemble.base.util import CustomDataType, DAValidationError, word
import re

class Charges(CustomDataType):
    name = 'charges'
    container_class = 'da-charges-container'
    input_class = 'da-charges'
    javascript = """\
$.validator.addMethod('charges', function(value, element, params){
    console.log('HHHHHHHHHHHHHHHHH1');
  return true;
});
"""
    jq_rule = 'charges'
    jq_message = 'You need to enter the charges.'
    print('HHHHHHHHHHHHHHHHH2')
    @classmethod
    def validate(cls, item):
        #item = str(item).strip()
        #m = re.search(r'^[0-9]{3}-?[0-9]{2}-?[0-9]{4}$', item)
        #if item == '' or m:
        return True
        #raise DAValidationError("A charge needs to be found in the database")