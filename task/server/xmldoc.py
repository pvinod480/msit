
import xml.dom.minidom


doc=xml.dom.minidom.Document()

main = doc.createElement('Employee')
doc.appendChild(main)

name = doc.createElement('name')
nameText=doc.createTextNode('vinod')
name.appendChild(nameText)
main.appendChild(name)

gender = doc.createElement('gender')
genderText=doc.createTextNode('male')
gender.appendChild(genderText)
main.appendChild(gender)

age = doc.createElement('age')
ageText=doc.createTextNode('22')
age.appendChild(ageText)
main.appendChild(age)

salary = doc.createElement('age')
salaryText=doc.createTextNode('22')
salary.appendChild(salaryText)
main.appendChild(salary)




print(doc.toprettyxml())
