# Create PDF with Fastapi and FPDF

##Backend
- Framework - FastAPI
- ORM - ORMAR
- DB - SQLite
- Create PDF - fpdf

## Start

- pip install -r req.txt
- uvicorn main:app
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/{id}  

The fpdf used, did not explicitly support Japanese  
The issues were two :  
1. While insertig non english data into the database unicode erroe thrown. 
While creating the sqlalchemy engine, add the convert_unicode parameter:  engine = sqlalchemy.create_engine("sqlite:///sqlite.db",convert_unicode=True,echo=True)  

2. The font did not support Japanese characters  
To add a font, download the .ttf file into a folder and add the font along with the path before setting the font where the text is written into the pdf.

