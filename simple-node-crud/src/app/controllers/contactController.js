const ContactRepository = require('../repositories/contactRepository')
require('express-async-errors')


class ContactController {
  async index(request, response){
    // Listar todos os registros
    const { orderBy = 'ASC'} = request.query // se orderBy == undefined ? orderBy == 'ASC'
    const direction = orderBy.toUpperCase() === 'DESC' ? 'DESC' : 'ASC'
    const contacts = await ContactRepository.findAll(orderBy)

    response.json(contacts)
  
  }

  async show(request, response){
    // Obter um registro

    //pegar id da rota
    const {id} = request.params;
    
    const contact = await ContactRepository.findById(id);

    if(!contact){
      // 404 - Not found
      return response.status(404).json({ error : 'User not found!'});
    }

    return response.json(contact);

  }

  async store(request, response){
    const { name, email, phone, category_id } = await request.body

    if(!name){
      return response.status(400).json({ error : 'Name is required!' });
    }

    const contactExist = await ContactRepository.findByEmail(email)
    
    if(contactExist.length){
      return response.status(400).json({ error : 'Contact already exists'})
    }

    const contact = await ContactRepository.create(request)
    response.json(contact)
  }               

  async update(request, response){
    // editar um registro
    const { id } = request.params
    const { name, email, phone, category_id} = request.body 

    const contactExist = await ContactRepository.findById(id)

    if(!contactExist){
      return response.status(404).json({ error : 'User not found!'});     
    }
    if(!name){
      return response.status(400).json({ error : 'Name is required!' });
    }

    const contactExistbyEmail = await ContactRepository.findByEmail(email)

    if(contactExistbyEmail && contactExistbyEmail.id === id){
      return response.status(400).json({ error : 'Email already in use'})
    }

    const contact = await ContactRepository.update(id, {name, email, phone, category_id})

    response.json(contact)
  }

  async delete(request, response){
    // deletar um registro
    const { id } = request.params;

    const contact = await ContactRepository.findById(id);

    if(!contact){
      // 404 - Not found
      return response.status(404).json({ error : 'User not found!'});
    }
    
    await ContactRepository.delete(id)
    response.sendStatus(204); // 204: No content but ok

  }


}

// Singleton
module.exports = new ContactController();
