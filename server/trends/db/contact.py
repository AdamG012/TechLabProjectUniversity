from trends.db.obj.contactModel import Contact


def add_contact_request(name, email, subject, content):
    c = Contact(name=name, email=email, subject=subject, content=content)
    c.save()
    return c
