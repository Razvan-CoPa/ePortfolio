import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { changeFilter } from "../../redux/filtersSlice";
import styles from "./Filter.module.css";

const Filter = () => {
  const dispatch = useDispatch();
  const filterValue = useSelector((state) => state.filters.name);

  const handleChange = (e) => {
    dispatch(changeFilter(e.target.value));
  };

  return (
    <div className={styles.filterContainer}>
      <label className={styles.label}>
        Filter contacts by name:
        <input
          type="text"
          value={filterValue}
          onChange={handleChange}
          className={styles.input}
        />
      </label>
    </div>
  );
};

export default Filter;
