from pydantic import BaseModel, EmailStr,Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str, Field(max_length=50,title='Name of the patient',description='abcd')]
  email: EmailStr
  age: int = Field(gt=0, lt=120)
  weight: Annotated[float, Field(gt=0,strict=True)]
  married: bool = False
  allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
  contact_details: Dict[str, str]


  @field_validator('name',mode='after')
  @classmethod
  def transform_name(cls,value):
    return value.upper()
  
  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError('Patient Older than 60 must have emergency contact')
    
    return model


def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('added into database')


patient_info = {'name':'nitish','email':'abc@gmail.com','age':65,'weight':75.3,'contact_details':{'phone':'376267'}}

patient1 = Patient(**patient_info)    #data validation - > Type coercion

insert_patient_data(patient1)