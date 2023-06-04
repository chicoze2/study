const { v4 } = require('uuid');
const db = require('../../database') // import o arquivo index

let contacts = require('../../mocks/users')

class ContactRepository{
  async findAll(orderBy) {

    const rows = await db.query(`
    SELECT contacts.*, categories.name AS category_name
    FROM contacts 
    LEFT JOIN categories ON categories.id = contacts.category_id 
    ORDER BY categories.name ${orderBy}`)

    // essa query possui bastante semântica SQL
    //Linha 1: SELECIONAR todas as colunas de contacts e selecionar categories.name COMO category_name

    //Linha 3: JUNTAR a tabela categories ONDE categories.id = contacts.category_id
    //ps. vide imagem joins.png

    return rows
  }

  async findById(id) {
    const rows = await db.query(`
    SELECT contacts.*, categories.name AS category_name
    FROM contacts 
    LEFT JOIN categories ON categories.id = contacts.category_id
    WHERE contacts.id = $1`,[id])
    return rows
  }

  async findByEmail(email) {
    const rows = await db.query('SELECT * FROM contacts WHERE email=$1',[email])
    return rows
  }

  async delete(id) {
    const deleteOp = await db.query(`
    DELETE FROM contacts WHERE id = $1`,[id])
    return deleteOp
  }

  async create(request) {

    const {name, email, phone, category_id} = request.body;

    const [row] = await db.query(`
    INSERT INTO contacts(name, email, phone, category_id)
    VALUES($1, $2, $3, $4)
    RETURNING *`,
    [name, email, phone, category_id])
  
    return row
  }

  async update(id, {name, email,   phone, category_id}) {
    const [row] = await db.query(`
    UPDATE contacts 
    SET name = $1, email = $2, phone = $3, category_id = $4
    WHERE id = $5
    RETURNING *`,
    [name, email, phone, category_id, id])
    return row
  }


}

module.exports = new ContactRepository();