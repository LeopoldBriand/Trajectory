import nodeModel from '../Model/nodeModel'; 
import { model } from 'mongoose'; 
const NodeModel = model('NodeModel', nodeModel); // Création du modèle à partir du schéma

function respond(err, result, res) { // Fonction utilisée tout au long du contrôleur pour répondre aux requetes
  if (err) {
    return res.status(500).json({error: err});
  }
  return res.json(result);
}

const nodeModelController = {
  getAll: (req, res) => {  // Récupérer tous les noeuds
    NodeModel.find({}, (err, NodeModels) => {
      return respond(err, NodeModels, res);
    });
  },
  create: (req, res) => { // Créer un noeud
    const newNodeModel = new NodeModel(req.body);
    newNodeModel.save((err, savedNodeModel) => {
      return respond(err, savedNodeModel, res);
    });
  },
  get: (req, res) => { // Récupérer un noeud
    NodeModel.findById(req.params.id, (err, NodeModel) => {
      return respond(err, NodeModel, res);
    });
  },
  update: (req, res) => { // Mettre à jour un noeud
    NodeModel.findByIdAndUpdate(req.params.id, req.body, (err, NodeModel) => {
      return respond(err, NodeModel, res);
    });
  },
  delete: (req, res) => { // Supprimer un noeud
    NodeModel.findByIdAndRemove(req.params.id, (err, NodeModel) => {
      return respond(err, NodeModel, res);
    });
  }
};

export default nodeModelController; // Export du contrôleur