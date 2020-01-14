import noeuds from '../Controller/nodeController';
import liaisons from '../Controller/linkController';

export default function(app) {

    // Noeuds
    app.route('/noeuds')
        .get(noeuds.getAll)
        .post(noeuds.create);

    app.route('/noeuds/:id')
        .get(noeuds.get)
        .put(noeuds.update)
        .delete(noeuds.delete);

    // Liaisons
    app.route('/liaisons')
        .get(liaisons.getAll)
        .post(liaisons.create);

    app.route('/liaisons/:id')
        .get(liaisons.get)
        .put(liaisons.update)
        .delete(liaisons.delete);

    app.use((req, res) => {res.status(404).json({url: req.originalUrl, error: 'not found'})});

};