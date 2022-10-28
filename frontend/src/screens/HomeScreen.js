import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Row, Col } from 'react-bootstrap';
import Book from '../components/Book';
import Message from '../components/Message';
import Loader from '../components/Loader';
import { listBooks } from '../actions/bookActions';
import { Link, useParams } from 'react-router-dom';
import Paginate from '../components/Paginate';
import BookCarousel from '../components/BookCarousel'; 

const HomeScreen = () => {
  const dispatch = useDispatch();
  const params = useParams();
  const keyword = params.keyword;
  //const pageNumber = params.pageNumber || 1;

  const bookList = useSelector((state) => state.bookList);
  //const { loading, error, books, page, pages } = bookList;
  const { loading, error, books } = bookList;
  console.log(books)

  useEffect(() => {
    dispatch(listBooks(keyword));
  }, [dispatch, keyword]);
  //[dispatch, keyword, pageNumber]);

  return (
    <>
      {/* {!keyword ? (
        <BookCarousel />
      ) : (
        <Link to="/" className="btn btn-light">
          Go Back
        </Link>
      )} */}
      <h1>Latest books</h1>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <>
          <Row>
            {books.map((book) => (
              <Col key={book._id} sm={12} md={6} lg={4} xl={3}>
                <Book book={book} />
              </Col>
            ))}
          </Row>
          {/* <Paginate
            pages={pages}
            page={page}
            keyword={keyword ? keyword : ''}
          /> */}
        </>
      )}
    </>
  );
};

export default HomeScreen;
