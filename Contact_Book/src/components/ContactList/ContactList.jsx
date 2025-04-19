// src/components/ContactList/ContactList.jsx

import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { deleteContact } from "../../redux/contactsOps";
import { selectFilteredContacts } from "../../redux/contactsSlice";
import styles from "./ContactList.module.css";

const ContactList = () => {
  const dispatch = useDispatch();
  const filteredContacts = useSelector(selectFilteredContacts);
  const { loading, error } = useSelector((state) => state.contacts);

  if (loading) {
    return <p>Loading contacts...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <ul className={styles.list}>
      {filteredContacts.map(({ id, name, phone }) => (
        <li key={id} className={styles.item}>
          <span>
            {name}: {phone}
          </span>
          <button
            className={styles.deleteButton}
            onClick={() => dispatch(deleteContact(id))}
          >
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
};

export default ContactList;
