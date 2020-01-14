import { Schema as _Schema } from 'mongoose'; // Import de la librairie mongoose
const Schema = _Schema;

// Définition du schéma
const projectSchema = new Schema({
    distance: {type: Number, required: true},
    source: {type: String, required: true, default: ''},
    destination : {type: String, required: true, default: ''},
    pattern: {type: String, required: true},
    arrow: {type: String, required: true},
    point: {type: Object, required: false}
  }, 
  {timestamps: true} // Pour avoir les dates de création et de modification automatiquement gérés par mongoose
);

export default projectSchema; // Export du schéma