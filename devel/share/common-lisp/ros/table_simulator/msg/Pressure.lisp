; Auto-generated. Do not edit!


(cl:in-package table_simulator-msg)


;//! \htmlinclude Pressure.msg.html

(cl:defclass <Pressure> (roslisp-msg-protocol:ros-message)
  ((hlive
    :reader hlive
    :initarg :hlive
    :type cl:fixnum
    :initform 0)
   (hstate
    :reader hstate
    :initarg :hstate
    :type cl:fixnum
    :initform 0)
   (hfinished
    :reader hfinished
    :initarg :hfinished
    :type cl:fixnum
    :initform 0)
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:fixnum
    :initform 0)
   (c1
    :reader c1
    :initarg :c1
    :type cl:fixnum
    :initform 0)
   (c2
    :reader c2
    :initarg :c2
    :type cl:fixnum
    :initform 0)
   (c3
    :reader c3
    :initarg :c3
    :type cl:fixnum
    :initform 0)
   (c4
    :reader c4
    :initarg :c4
    :type cl:fixnum
    :initform 0)
   (c5
    :reader c5
    :initarg :c5
    :type cl:fixnum
    :initform 0)
   (c6
    :reader c6
    :initarg :c6
    :type cl:fixnum
    :initform 0)
   (c7
    :reader c7
    :initarg :c7
    :type cl:fixnum
    :initform 0)
   (c8
    :reader c8
    :initarg :c8
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Pressure (<Pressure>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Pressure>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Pressure)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name table_simulator-msg:<Pressure> is deprecated: use table_simulator-msg:Pressure instead.")))

(cl:ensure-generic-function 'hlive-val :lambda-list '(m))
(cl:defmethod hlive-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:hlive-val is deprecated.  Use table_simulator-msg:hlive instead.")
  (hlive m))

(cl:ensure-generic-function 'hstate-val :lambda-list '(m))
(cl:defmethod hstate-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:hstate-val is deprecated.  Use table_simulator-msg:hstate instead.")
  (hstate m))

(cl:ensure-generic-function 'hfinished-val :lambda-list '(m))
(cl:defmethod hfinished-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:hfinished-val is deprecated.  Use table_simulator-msg:hfinished instead.")
  (hfinished m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:pressure-val is deprecated.  Use table_simulator-msg:pressure instead.")
  (pressure m))

(cl:ensure-generic-function 'c1-val :lambda-list '(m))
(cl:defmethod c1-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c1-val is deprecated.  Use table_simulator-msg:c1 instead.")
  (c1 m))

(cl:ensure-generic-function 'c2-val :lambda-list '(m))
(cl:defmethod c2-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c2-val is deprecated.  Use table_simulator-msg:c2 instead.")
  (c2 m))

(cl:ensure-generic-function 'c3-val :lambda-list '(m))
(cl:defmethod c3-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c3-val is deprecated.  Use table_simulator-msg:c3 instead.")
  (c3 m))

(cl:ensure-generic-function 'c4-val :lambda-list '(m))
(cl:defmethod c4-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c4-val is deprecated.  Use table_simulator-msg:c4 instead.")
  (c4 m))

(cl:ensure-generic-function 'c5-val :lambda-list '(m))
(cl:defmethod c5-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c5-val is deprecated.  Use table_simulator-msg:c5 instead.")
  (c5 m))

(cl:ensure-generic-function 'c6-val :lambda-list '(m))
(cl:defmethod c6-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c6-val is deprecated.  Use table_simulator-msg:c6 instead.")
  (c6 m))

(cl:ensure-generic-function 'c7-val :lambda-list '(m))
(cl:defmethod c7-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c7-val is deprecated.  Use table_simulator-msg:c7 instead.")
  (c7 m))

(cl:ensure-generic-function 'c8-val :lambda-list '(m))
(cl:defmethod c8-val ((m <Pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:c8-val is deprecated.  Use table_simulator-msg:c8 instead.")
  (c8 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Pressure>) ostream)
  "Serializes a message object of type '<Pressure>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hlive)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hstate)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hfinished)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pressure)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c5)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c6)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c7)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c8)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Pressure>) istream)
  "Deserializes a message object of type '<Pressure>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hlive)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hstate)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'hfinished)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pressure)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c5)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c6)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c7)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'c8)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Pressure>)))
  "Returns string type for a message object of type '<Pressure>"
  "table_simulator/Pressure")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Pressure)))
  "Returns string type for a message object of type 'Pressure"
  "table_simulator/Pressure")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Pressure>)))
  "Returns md5sum for a message object of type '<Pressure>"
  "5906d18d24109eb2a3d96dd40630f985")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Pressure)))
  "Returns md5sum for a message object of type 'Pressure"
  "5906d18d24109eb2a3d96dd40630f985")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Pressure>)))
  "Returns full string definition for message of type '<Pressure>"
  (cl:format cl:nil "uint8 hlive~%uint8 hstate~%uint8 hfinished~%uint8 pressure~%uint8 c1~%uint8 c2~%uint8 c3~%uint8 c4~%uint8 c5~%uint8 c6~%uint8 c7~%uint8 c8~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Pressure)))
  "Returns full string definition for message of type 'Pressure"
  (cl:format cl:nil "uint8 hlive~%uint8 hstate~%uint8 hfinished~%uint8 pressure~%uint8 c1~%uint8 c2~%uint8 c3~%uint8 c4~%uint8 c5~%uint8 c6~%uint8 c7~%uint8 c8~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Pressure>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Pressure>))
  "Converts a ROS message object to a list"
  (cl:list 'Pressure
    (cl:cons ':hlive (hlive msg))
    (cl:cons ':hstate (hstate msg))
    (cl:cons ':hfinished (hfinished msg))
    (cl:cons ':pressure (pressure msg))
    (cl:cons ':c1 (c1 msg))
    (cl:cons ':c2 (c2 msg))
    (cl:cons ':c3 (c3 msg))
    (cl:cons ':c4 (c4 msg))
    (cl:cons ':c5 (c5 msg))
    (cl:cons ':c6 (c6 msg))
    (cl:cons ':c7 (c7 msg))
    (cl:cons ':c8 (c8 msg))
))
