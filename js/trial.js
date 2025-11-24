const trials = {
    "instructions": ["instructions.png"],
    "order_1": {
        // Intentional condition
        "chain": {
            "story": ["chain_v1/chain_intent.001.png", "chain_v1/chain_intent.002.png", "chain_v1/chain_intent.003.png", "chain_v1/chain_intent.004.png", "chain_v1/chain_intent.005.png", "chain_v1/chain_intent.006.png", "chain_v1/chain_intent.007.png", "chain_v1/chain_intent.008.png"],
            "questions": {
                "cause": "chain_v1/chain_intentional_q_cause.png",
                "simple": "chain_v1/chain_intentional_q_simple.png",
                "fault": "chain_v1/chain_intentional_q_fault.png",
                "punishment": "chain_v1/chain_intentional_q_punishment.png"
            },
        },
    },
    "order_2": {
        // Accidental condition
        "chain": {
            "story": ["chain_v1/chain_accident.001.png", "chain_v1/chain_accident.002.png", "chain_v1/chain_accident.003.png", "chain_v1/chain_accident.004.png", "chain_v1/chain_accident.005.png", "chain_v1/chain_accident.006.png", "chain_v1/chain_accident.007.png", "chain_v1/chain_accident.008.png"],
            "questions": {
                "cause": "chain_v1/chain_accidental_q_cause.png",
                "simple": "chain_v1/chain_accidental_q_simple.png",
                "fault": "chain_v1/chain_accidental_q_fault.png",
                "punishment": "chain_v1/chain_accidental_q_punishment.png"
            },
        },
    },
}
