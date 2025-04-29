import streamlit as st
import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(len(self.chain), prev_block.hash, time.time(), data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

# Initialize blockchain
if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

st.title("🧱 Simple Blockchain Ledger")

# Form to add a new block
with st.form("Add Block"):
    new_data = st.text_input("Enter transaction data:")
    submitted = st.form_submit_button("Add Block")
    if submitted:
        if new_data:
            st.session_state.blockchain.add_block(new_data)
            st.success("Block added successfully!")
        else:
            st.error("Please enter some data.")

# Show blockchain
st.subheader("📜 Blockchain Ledger")
for block in st.session_state.blockchain.chain:
    st.json({
        "Index": block.index,
        "Timestamp": time.ctime(block.timestamp),
        "Data": block.data,
        "Hash": block.hash,
        "Previous Hash": block.previous_hash
    })

# Validate chain
st.subheader("🔍 Validate Chain")
if st.button("Check if blockchain is valid"):
    is_valid =_
