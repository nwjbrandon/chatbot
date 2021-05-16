from flask import request

def upload_model_service():
    f = request.files["file"]
    filename = f.filename
    f.save(filename)
    return {"message": f"{filename} uploaded successfully"}


def upload_program_script_service(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return {"message": f"{filename} uploaded successfully"}
