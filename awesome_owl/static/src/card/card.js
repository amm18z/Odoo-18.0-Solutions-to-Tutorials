import { Component, useState } from "@odoo/owl";

export class Card extends Component {
    static template = "awesome_owl.card";

    static props = {
        title: String,
        content: String
    };

    setup() {
        // this.state = useState({  });
        // not setting anything up yet really
    }

    
}