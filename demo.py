from umsc import UgMultiScriptConverter

converter = UgMultiScriptConverter('CTS', 'IPA')

input = "encür"

print(converter(input))
