import linkModel from '../Model/linkModel'; 
import { model } from 'mongoose'; 
const LinkModel = model('LinkModel', linkModel); // Création du modèle à partir du schéma

function respond(err, result, res) { // Fonction utilisée tout au long du contrôleur pour répondre aux requetes
  if (err) {
    return res.status(500).json({error: err});
  }
  return res.json(result);
}

const linkModelController = {
  getAll: (req, res) => {  // Récupérer tous les liaisons
    LinkModel.find({}, (err, LinkModels) => {
      return respond(err, LinkModels, res);
    });
  },
  create: (req, res) => { // Créer un liaison
    const newLinkModel = new LinkModel(req.body);
    newLinkModel.save((err, savedLinkModel) => {
      return respond(err, savedLinkModel, res);
    });
  },
  get: (req, res) => { // Récupérer un liaison
    LinkModel.findById(req.params.id, (err, LinkModel) => {
      return respond(err, LinkModel, res);
    });
  },
  update: (req, res) => { // Mettre à jour un liaison
    LinkModel.findByIdAndUpdate(req.params.id, req.body, (err, LinkModel) => {
      return respond(err, LinkModel, res);
    });
  },
  delete: (req, res) => { // Supprimer un liaison
    LinkModel.findByIdAndRemove(req.params.id, (err, LinkModel) => {
      return respond(err, LinkModel, res);
    });
  }
};

export default linkModelController; // Export du contrôleur