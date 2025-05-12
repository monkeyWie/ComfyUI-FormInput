class TextInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "process_text"
    CATEGORY = "FormInput"

    def process_text(self, text):
        return (text,)


class BooleanInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "boolean": ("BOOLEAN", {"default": True, "label_on": "True", "label_off": "False"}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("boolean_output",)
    FUNCTION = "process_boolean"
    CATEGORY = "FormInput"

    def process_boolean(self, boolean):
        return (boolean,)


class DisplayTextNode:
    OUTPUT_NODE = True  # Mark as an output/display node

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_to_display": ("STRING", {"multiline": True, "default": "Text to display"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("displayed_text",)
    FUNCTION = "display_the_text"
    OUTPUT_NODE = True
    CATEGORY = "FormInput"

    def display_the_text(self, text_to_display):
        # This structure allows the text to be shown in the node's UI (if supported)
        # and also passes the text as a regular output.
        return {"ui": {"text": [text_to_display]}, "result": (text_to_display,)}


NODE_CLASS_MAPPINGS = {
    "TextInput_FormInput": TextInputNode,
    "BooleanInput_FormInput": BooleanInputNode,
    "DisplayText_FormInput": DisplayTextNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextInput_FormInput": "Text Input (FormInput)",
    "BooleanInput_FormInput": "Boolean Input (FormInput)",
    "DisplayText_FormInput": "Display Text (FormInput)",
}
