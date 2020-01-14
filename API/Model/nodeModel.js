import { Schema as _Schema } from 'mongoose'; // Import de la librairie mongoose
const Schema = _Schema;

// Définition du schéma
const eventSchema = new Schema(
  {
    name: { type: String, required: true },
    color: { type: String, required: false },
    liaisons: { type: Array, required: true },
    point: { type: Object, required: true },
    width: { type: Number, required: true },
    height: { type: Number, required: true },
    shape: { type: String, required: true },
  },
  { timestamps: true } // Pour avoir les dates de création et de modification automatiquement gérés par mongoose
);

export default eventSchema; // Export du schéma