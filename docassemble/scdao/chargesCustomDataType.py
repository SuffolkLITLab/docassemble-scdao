from docassemble.base.util import CustomDataType, DAValidationError, word
import re

class Charges(CustomDataType):
    name = 'charges'
    container_class = 'da-charges-container'
    input_class = 'magicsearch multi'
    javascript = """\
    $("#basic").magicsearch({
    dataSource: dataSource,
    multiple: true,
    fields: ["firstName","lastName"],
    multiField: "firstName",
    id:"id",
    format:"%firstName% · %lastName%"});
    """

    jq_rule = 'charges'
    jq_message = 'You need to enter the charges.'

    @classmethod
    def validate(cls, item):
        #item = str(item).strip()
        #m = re.search(r'^[0-9]{3}-?[0-9]{2}-?[0-9]{4}$', item)
        #if item == '' or m:
        return True
        #raise DAValidationError("A charge needs to be found in the database")
