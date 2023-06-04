const categoriesRepository = require('../repositories/categoryRepository')
require('express-async-errors')

class CategoryController{
  async index(request, response) {
    const categories = await categoriesRepository.findAll()
    response.json(categories)
  }

  async show(request, response) {
    const { id } = request.params

    const category = await categoriesRepository.findById(id)

    console.log(category)

    if(!category){
      return response.status(404).json({ message: 'Category not found'})
    }

    return response.json(category)
  }

  async store(request, response) {
    const { name } = request.body;

    if(!name){
      return response.status(400).json({ error: 'Name is required'})
    }

    const category = await categoriesRepository.create({ name })

    response.json(category)
  }

  async delete(request, response) {
    const {id} = request.params
    
    if(!id){
      return response.status(400).json({ error: 'Invalid ID'})
    }

    const categoryExists = await categoriesRepository.findById(id)

    console.log(categoryExists)

    if(!categoryExists.length){
      return response.status(404).json({ message: 'Category not found'})
    }

    const del = await categoriesRepository.delete(id)

    return response.status(204).json(del)

  }

  async update(request, response) {
    const { id } = request.params
    const { name } = request.body
    
    //verific name
    if(!name){
      return response.status(400).json({ error: 'Name is required'})
    }

    //verific existencia

    const categoryExists = await categoriesRepository.findById(id)

    if(!categoryExists.length){
      return response.status(404).json({ message: 'Category not found'})
    }

    //repositorie .update
    const category = await categoriesRepository.update({id}, {name})

    return response.json(category)

  }

}

module.exports = new CategoryController()